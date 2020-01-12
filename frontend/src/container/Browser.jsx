import React from 'react';
import { makeStyles } from "@material-ui/core/styles";

import BrowserNav from './BrowserNav'


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
        </div>
    )
}

export default Browser;
