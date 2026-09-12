from pathlib import Path

path = Path('status-settings.html')
text = path.read_text(encoding='utf-8')
marker = 'status-settings-mobile-containment-final'
if marker not in text:
    text += r'''
<style id="status-settings-mobile-containment-final">
#influenza-admin-mock .admin-status-page-v1,
#influenza-admin-mock .admin-settings-v1,
#influenza-admin-mock .admin-settings-v1-row,
#influenza-admin-mock .admin-setting-v1-card,
#influenza-admin-mock .admin-setting-v1-body,
#influenza-admin-mock .admin-setting-v1-form,
#influenza-admin-mock .admin-setting-v1-field,
#influenza-admin-mock .admin-basic-schedule-v1,
#influenza-admin-mock .admin-basic-schedule-v1-scroll{
  min-width:0!important;
  max-width:100%!important;
  box-sizing:border-box!important;
}
#influenza-admin-mock .admin-setting-v1-card{width:100%!important;overflow:hidden!important}
#influenza-admin-mock .admin-setting-v1-field input,
#influenza-admin-mock .admin-setting-v1-field select,
#influenza-admin-mock .admin-setting-v1-field textarea{
  width:100%!important;
  min-width:0!important;
  max-width:100%!important;
  box-sizing:border-box!important;
}
#influenza-admin-mock .admin-basic-schedule-v1{overflow:hidden!important}
#influenza-admin-mock .admin-basic-schedule-v1-scroll{
  width:100%!important;
  min-width:0!important;
  max-width:100%!important;
  overflow-x:auto!important;
  overflow-y:hidden!important;
  -webkit-overflow-scrolling:touch!important;
}
@media(max-width:900px){
  html,body{width:100%!important;max-width:100%!important;overflow-x:hidden!important}
  #influenza-admin-mock,
  #influenza-admin-mock .admin-shell,
  #influenza-admin-mock .admin-main,
  #influenza-admin-mock .admin-status-page-v1{
    width:100%!important;
    min-width:0!important;
    max-width:100%!important;
    overflow-x:hidden!important;
  }
  #influenza-admin-mock .admin-basic-schedule-v1-table{
    width:620px!important;
    min-width:620px!important;
    max-width:none!important;
  }
  #influenza-admin-mock .admin-setting-v1-record{
    min-width:0!important;
    max-width:100%!important;
    grid-template-columns:minmax(0,1fr) auto!important;
  }
  #influenza-admin-mock .admin-setting-v1-record>div:first-child{
    min-width:0!important;
    overflow-wrap:anywhere!important;
  }
}
</style>
'''
    path.write_text(text, encoding='utf-8')
