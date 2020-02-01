import React from "react";
import "date-fns";
import { makeStyles } from "@material-ui/core/styles";

import Grid from "@material-ui/core/Grid";
import DateFnsUtils from "@date-io/date-fns";
import TextField from "@material-ui/core/TextField";
import Fab from "@material-ui/core/Fab";
import AddIcon from "@material-ui/icons/Add";
import {
  MuiPickersUtilsProvider,
  KeyboardTimePicker,
  KeyboardDatePicker
} from "@material-ui/pickers";
import DateRange from "./DateRange";

const useStyles = makeStyles({
  datePicker: { width: 150, marginRight: 20 },
  timePicker: { width: 100 },
  collectionName: {
    width: 150,
    marginLeft: 10,
    marginRight: 10
  },
  sampleSize: { width: 100, marginLeft: 10, marginRight: 10 }
});

const AddCollection = ({ onCollectionAdd, classes }) => {
  const [collectionName, setCollectionName] = React.useState();
  const [sampleSize, setSampleSize] = React.useState();
  return (
    <>
      <form noValidate autoComplete="off">
        <TextField
          className={classes.collectionName}
          id="standard-basic"
          label="Collection Name"
          value={collectionName}
          onChange={event => setCollectionName(event.target.value)}
        />
        <TextField
          className={classes.sampleSize}
          id="standard-basic"
          label="Sample Size"
          value={sampleSize}
          onChange={event => setSampleSize(event.target.value)}
        />
      </form>
      <Fab color="primary" aria-label="add">
        <AddIcon
          onClick={() => onCollectionAdd({ collectionName, sampleSize })}
        />
      </Fab>
    </>
  );
};

const DateTimePicker = ({ date, setDate, label, classes }) => (
  <>
    <MuiPickersUtilsProvider utils={DateFnsUtils}>
      <KeyboardDatePicker
        className={classes.datePicker}
        disableToolbar
        variant="inline"
        format="MM/dd/yyyy"
        margin="normal"
        label={`${label} Date`}
        value={date}
        onChange={setDate}
        KeyboardButtonProps={{
          "aria-label": "change date"
        }}
      />
      <KeyboardTimePicker
        className={classes.timePicker}
        disableToolbar
        variant="inline"
        margin="normal"
        label={`${label} Time`}
        value={date}
        onChange={setDate}
        KeyboardButtonProps={{
          "aria-label": "change time"
        }}
      />
    </MuiPickersUtilsProvider>
  </>
);

const BrowserNav = ({ search, onSearchUpdate, onAddCollection }) => {
  const classes = useStyles();
  return (
    <Grid container justify="space-around" alignItems="flex-end" spacing={5}>
      <Grid container item xs={4} spacing={3}>
        <DateTimePicker
          date={search.startDate}
          setDate={startDate => onSearchUpdate({ startDate })}
          label="Start"
          classes={classes}
        />
      </Grid>
      <Grid container item xs={4} spacing={3}>
        <DateTimePicker
          date={search.endDate}
          setDate={endDate => onSearchUpdate({ endDate })}
          label="End"
          classes={classes}
        />
      </Grid>
      <Grid container item xs={4} spacing={3}>
        <AddCollection
          // TODO
          //   onAdd={() => onAddCollection(search)}
          classes={classes}
        />
      </Grid>
      <Grid container item xs={12} spacing={3}>
        <DateRange
          startDate={search.startDate}
          setStartDate={startDate => onSearchUpdate({ startDate })}
          endDate={search.endDate}
          setEndDate={endDate => onSearchUpdate({ endDate })}
        />
      </Grid>
    </Grid>
  );
};

export default BrowserNav;
