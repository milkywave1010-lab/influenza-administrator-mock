from pathlib import Path
import re

p = Path('status-settings.html')
s = p.read_text(encoding='utf-8')

# 過去の応急CSSを除去し、最終版へ一本化する。
for style_id in ('status-settings-mobile-containment-final', 'status-settings-mobile-fit-all-final', 'status-settings-mobile-polish-final'):
    s = re.sub(r'<style id="' + re.escape(style_id) + r'">.*?</style>\s*', '', s, flags=re.S)

final_css = r'''<style id="status-settings-mobile-polish-final">
/* 公開モック最終調整：全要素を画面内に収容し、横はみ出しを禁止 */
html,body{
  width:100%;
  max-width:100%;
  overflow-x:hidden;
}
#influenza-admin-mock,
#influenza-admin-mock .admin-shell,
#influenza-admin-mock .admin-main,
#influenza-admin-mock .admin-status-page-v1,
#influenza-admin-mock .admin-settings-v1,
#influenza-admin-mock .admin-settings-v1-row,
#influenza-admin-mock .admin-setting-v1-card,
#influenza-admin-mock .admin-setting-v1-body,
#influenza-admin-mock .admin-setting-v1-form,
#influenza-admin-mock .admin-setting-v1-field,
#influenza-admin-mock .admin-setting-v1-record,
#influenza-admin-mock .admin-basic-schedule-v1,
#influenza-admin-mock .admin-basic-schedule-v1-scroll{
  min-width:0;
  max-width:100%;
  box-sizing:border-box;
}
#influenza-admin-mock .admin-setting-v1-card{width:100%;overflow:hidden}
#influenza-admin-mock .admin-setting-v1-field input,
#influenza-admin-mock .admin-setting-v1-field select,
#influenza-admin-mock .admin-setting-v1-field textarea{
  display:block;
  width:100%;
  min-width:0;
  max-width:100%;
  box-sizing:border-box;
}
#influenza-admin-mock .admin-setting-v1-record>div:first-child{min-width:0}
#influenza-admin-mock .admin-setting-v1-record b,
#influenza-admin-mock .admin-setting-v1-record span{overflow-wrap:anywhere;word-break:break-word}

@media(max-width:900px){
  #influenza-admin-mock .admin-shell{
    width:100%;
    max-width:100%;
    padding:10px;
    overflow-x:hidden;
  }
  #influenza-admin-mock .admin-main,
  #influenza-admin-mock .admin-status-page-v1{
    width:100%;
    max-width:100%;
    overflow-x:hidden;
  }
  #influenza-admin-mock .admin-main-tabs{
    width:100%;
    min-width:0;
    max-width:100%;
    grid-template-columns:1fr;
  }
  #influenza-admin-mock .admin-main-tab{
    width:100%;
    min-width:0;
    max-width:100%;
  }
  #influenza-admin-mock .admin-status-v1-grid{grid-template-columns:1fr}
  #influenza-admin-mock .admin-status-v1-panel,
  #influenza-admin-mock .admin-status-v1-body{min-width:0;max-width:100%;overflow:hidden}
  #influenza-admin-mock .admin-status-v1-log{
    grid-template-columns:52px 78px minmax(0,1fr);
    gap:6px;
    min-width:0;
    padding:11px 2px;
    font-size:11px;
  }
  #influenza-admin-mock .admin-status-v1-log>*{min-width:0;overflow-wrap:anywhere}
  #influenza-admin-mock .admin-status-v1-log .ok{grid-column:3;text-align:right}

  #influenza-admin-mock .admin-settings-v1-row{grid-template-columns:1fr}
  #influenza-admin-mock .admin-setting-v1-body{padding:14px 12px 16px}
  #influenza-admin-mock .admin-setting-v1-form{grid-template-columns:1fr}
  #influenza-admin-mock .admin-setting-v1-field.full{grid-column:auto}

  #influenza-admin-mock .admin-basic-schedule-v1{width:100%;overflow:hidden}
  #influenza-admin-mock .admin-basic-schedule-v1-head{
    align-items:flex-start;
    flex-direction:column;
    gap:4px;
  }
  #influenza-admin-mock .admin-basic-schedule-v1-scroll{
    width:100%;
    min-width:0;
    max-width:100%;
    overflow:hidden;
  }
  #influenza-admin-mock .admin-basic-schedule-v1-table{
    width:100%;
    min-width:0;
    max-width:100%;
    table-layout:fixed;
    border-collapse:collapse;
  }
  #influenza-admin-mock .admin-basic-schedule-v1-table th,
  #influenza-admin-mock .admin-basic-schedule-v1-table td{
    min-width:0;
    width:auto;
    padding:7px 1px;
    font-size:11px;
    overflow:hidden;
    white-space:nowrap;
    text-overflow:clip;
  }
  #influenza-admin-mock .admin-basic-schedule-v1-table th:first-child,
  #influenza-admin-mock .admin-basic-schedule-v1-table td:first-child{width:62px}
  #influenza-admin-mock .admin-basic-schedule-v1-table input[type="checkbox"]{
    display:inline-block;
    width:18px;
    min-width:18px;
    max-width:18px;
    height:18px;
    margin:0;
    padding:0;
    vertical-align:middle;
  }

  #influenza-admin-mock .admin-setting-v1-actions{
    display:grid;
    grid-template-columns:repeat(2,minmax(0,1fr));
    width:100%;
    min-width:0;
    max-width:100%;
    gap:8px;
  }
  #influenza-admin-mock .admin-setting-v1-actions:has(>button:only-child){grid-template-columns:1fr}
  #influenza-admin-mock .admin-setting-v1-actions button{
    width:100%;
    min-width:0;
    max-width:100%;
    white-space:normal;
    line-height:1.3;
  }

  #influenza-admin-mock .admin-setting-v1-record{
    width:100%;
    min-width:0;
    max-width:100%;
    grid-template-columns:1fr;
    gap:9px;
  }
  #influenza-admin-mock .admin-setting-v1-record .buttons{
    display:grid;
    grid-template-columns:repeat(2,minmax(0,1fr));
    width:100%;
    min-width:0;
    gap:7px;
  }
  #influenza-admin-mock .admin-setting-v1-record .buttons button{
    width:100%;
    min-width:0;
    max-width:100%;
  }
  #influenza-admin-mock .mock-note{overflow-wrap:anywhere}
}

@media(max-width:380px){
  #influenza-admin-mock .admin-shell{padding:8px}
  #influenza-admin-mock .admin-setting-v1-card>summary{padding:14px 12px}
  #influenza-admin-mock .admin-setting-v1-body{padding:12px 10px 14px}
  #influenza-admin-mock .admin-basic-schedule-v1-table th,
  #influenza-admin-mock .admin-basic-schedule-v1-table td{font-size:10px;padding:6px 0}
  #influenza-admin-mock .admin-basic-schedule-v1-table th:first-child,
  #influenza-admin-mock .admin-basic-schedule-v1-table td:first-child{width:56px}
  #influenza-admin-mock .admin-basic-schedule-v1-table input[type="checkbox"]{
    width:17px;
    min-width:17px;
    max-width:17px;
    height:17px;
  }
}
</style>
'''

pos = s.find('</head>')
if pos < 0:
    raise SystemExit('</head> not found')
s = s[:pos] + final_css + s[pos:]
p.write_text(s, encoding='utf-8')
