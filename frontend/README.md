branch 'restructure':
    Index
      Browser (is a QueryRenderer)
        DateRange (only this.state start/end dates)
        FrameGrid (props.frames)

problem hier: DateRange ist teil des loading states


branch 'stefan-master'
    Index
       Browser
         BrowserNav
         DateRange
         Frames (is QueryRenderer)
