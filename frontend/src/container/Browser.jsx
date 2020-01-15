import React from 'react';
import { makeStyles } from "@material-ui/core/styles";

import BrowserNav from './BrowserNav'
import Frames from './Frames'


const useStyles = makeStyles({
    root: {
    }
}
);

const Browser = () => {
    const classes = useStyles();
    return (
        <div className={classes.root}>
            <BrowserNav/>
            <Frames/>
        </div>
    )
}

export default Browser;
