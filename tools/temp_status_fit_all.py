from pathlib import Path
p=Path('status-settings.html')
s=p.read_text(encoding='utf-8')
marker='status-settings-mobile-fit-all-final'
if marker not in s:
    block=r'''<style id="status-settings-mobile-fit-all-final">
@media(max-width:900px){
  #influenza-admin-mock .admin-basic-schedule-v1-scroll{
    width:100%!important;
    min-width:0!important;
    max-width:100%!important;
    overflow-x:hidden!important;
  }
  #influenza-admin-mock .admin-basic-schedule-v1-table{
    width:100%!important;
    min-width:0!important;
    max-width:100%!important;
    table-layout:fixed!important;
  }
  #influenza-admin-mock .admin-basic-schedule-v1-table th,
  #influenza-admin-mock .admin-basic-schedule-v1-table td{
    min-width:0!important;
    width:auto!important;
    padding:7px 2px!important;
    font-size:11px!important;
    overflow:hidden!important;
    text-overflow:clip!important;
    white-space:nowrap!important;
  }
  #influenza-admin-mock .admin-basic-schedule-v1-table th:first-child,
  #influenza-admin-mock .admin-basic-schedule-v1-table td:first-child{
    width:68px!important;
  }
  #influenza-admin-mock .admin-basic-schedule-v1-table input[type="checkbox"]{
    width:18px!important;
    height:18px!important;
    max-width:18px!important;
  }
  #influenza-admin-mock .admin-setting-v1-actions{
    width:100%!important;
    min-width:0!important;
    max-width:100%!important;
    flex-wrap:wrap!important;
  }
  #influenza-admin-mock .admin-setting-v1-actions button{
    min-width:0!important;
    max-width:100%!important;
  }
}
</style>'''
    pos=s.find('</head>')
    if pos<0: raise SystemExit('</head> not found')
    s=s[:pos]+block+'\n'+s[pos:]
    p.write_text(s,encoding='utf-8')
