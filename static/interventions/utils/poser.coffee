class Denigma.RowPoser

  constructor: (@rowMargin,@rowHeight,@marginX)->

    #indian-like code warning: all these pos functions are inaccurate and mostly wrong
  getTopPos: (d,i)=> i* @rowHeight+i*@rowMargin/2
  getBottomPos: (d,i)=> (i+1)* (@rowHeight+@rowMargin)-@rowMargin*2

  getMiddlePos: (h=0)=>
    (d,i)=> i * @rowHeight+i* @rowMargin / 2  + @contentHeight() / 2 - @rowMargin / 4 - h/2


  makeCentered: (fun,h)=>
    ###
      Makes position function centered
    ###
    (d,i)=>fun(d,i)-h/2

  contentHeight: => @rowHeight-@rowMargin/2
