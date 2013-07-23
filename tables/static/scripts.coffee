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
  $(".grids").mCustomScrollbar(verParams)

  horParams = params
  horParams.horizontalScroll = true
  #$("#chatboard").mCustomScrollbar(horParams)

Denigma.on "run", =>
  addScrolling()