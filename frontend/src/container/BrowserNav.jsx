import React from 'react';
import 'date-fns';
import Grid from '@material-ui/core/Grid';
import DateFnsUtils from '@date-io/date-fns';
import {
  MuiPickersUtilsProvider,
  KeyboardTimePicker,
  KeyboardDatePicker,
} from '@material-ui/pickers';

const BrowserNav = () => {
  // The first commit of Material-UI
  const [startDate, setStartDate] = React.useState(new Date('2014-08-18T21:11:54'));
  const [endDate, setEndDate] = React.useState(new Date('2014-08-18T21:11:54'));


//   const handleDateChange = date => {
//     setSelectedDate(date);
//   };

  return (
    <MuiPickersUtilsProvider utils={DateFnsUtils}>
      <Grid container justify="space-around">
        <KeyboardDatePicker
          disableToolbar
          variant="inline"
          format="MM/dd/yyyy"
          margin="normal"
          label="Start Date"
          value={startDate}
          onChange={setStartDate}
          KeyboardButtonProps={{
            'aria-label': 'change date',
          }}
        />
        <KeyboardTimePicker
          disableToolbar
          variant="inline"
          margin="normal"
          label="Start Time"
          value={startDate}
          onChange={setStartDate}
          KeyboardButtonProps={{
            'aria-label': 'change time',
          }}
        />
        <KeyboardDatePicker
          disableToolbar
          variant="inline"
          format="MM/dd/yyyy"
          margin="normal"
          label="End Date"
          value={endDate}
          onChange={setEndDate}
          KeyboardButtonProps={{
            'aria-label': 'change date',
          }}
        />
        <KeyboardTimePicker
          disableToolbar
          variant="inline"
          margin="normal"
          label="End Time"
          value={endDate}
          onChange={setEndDate}
          KeyboardButtonProps={{
            'aria-label': 'change time',
          }}
        />
      </Grid>
    </MuiPickersUtilsProvider>
  );
}

export default BrowserNav;
