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

    const [startDate, setStartDate] = React.useState(new Date('2019-11-15T00:00:00'));
    const [endDate, setEndDate] = React.useState(new Date('2019-11-17T00:00:00'));

    return (
        <div className={classes.root}>
            <BrowserNav
                startDate={startDate}
                setStartDate={setStartDate}
                endDate={endDate}
                setEndDate={setEndDate}
                />
            <Frames startDate={startDate} endDate={endDate}/>
        </div>
    )
}

export default Browser;
