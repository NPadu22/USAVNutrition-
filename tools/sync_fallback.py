"""Rebuild index.html's built-in <script id="af-data"> from sheet tabs (JSON of tab -> rows incl. header),
by running the app's own sheet loader against mocked gviz responses."""
import json,re,sys
from urllib.parse import urlparse,parse_qs
from playwright.sync_api import sync_playwright
html_path,tabs_path=sys.argv[1],sys.argv[2]
tabs=json.load(open(tabs_path))
def gviz(cb,rows):
    head=rows[0]; body=rows[1:]
    t={"cols":[{"label":h} for h in head],"rows":[{"c":[({"v":(r[i] if i<len(r) else ""),"f":None} if i<len(r) and r[i]!="" else None) for i in range(len(head))]} for r in body]}
    return f"{cb}({json.dumps({'status':'ok','table':t})})"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page()
    def handle(route):
        u=urlparse(route.request.url)
        if "gviz" in u.path:
            q=parse_qs(u.query); tq=q["tqx"][0]; cb=tq.split("responseHandler:")[1]; sheet=q["sheet"][0]
            return route.fulfill(status=200,content_type="text/javascript",body=gviz(cb,tabs[sheet]))
        route.abort()
    pg.route("https://**/*",handle)
    pg.add_init_script("localStorage.clear()")
    pg.goto("file://"+html_path); pg.wait_for_function("localStorage.getItem('af_sheet')",timeout=15000)
    data=pg.evaluate("localStorage.getItem('af_sheet')"); b.close()
s=open(html_path).read()
obj=json.loads(data); out=json.dumps(obj,ensure_ascii=False).replace("</","<\\/")
s2=re.sub(r'(<script type="application/json" id="af-data">)(.*?)(</script>)',lambda m:m.group(1)+out+m.group(3),s,count=1,flags=re.S)
assert s2!=s or True
open(html_path,"w").write(s2)
print("announcements:",[a["t"] for a in obj["announcements"]],"| lunch weeks:",len(obj["cycles"]["Lunch"]),"| snack weeks:",len(obj["snackCycle"]),"| recipes:",len(obj["smoothieRecipes"]))
