addScrolling = =>

  params =
    theme:"dark-thick"
    advanced:
      updateOnContentResize: true
      autoScrollOnFocus: true
      updateOnContentResize: true
      updateOnBrowserResize:true
      autoHideScrollbar:true
    scrollButtons:{
      enable: true
    }

  verParams = params
  $(".grid").mCustomScrollbar(verParams)

  horParams = params
  horParams.horizontalScroll = true
  #$("#chatboard").mCustomScrollbar(horParams)

Denigma.on "run", =>
  addScrolling()