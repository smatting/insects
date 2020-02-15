import BugReportOutlinedIcon from "@material-ui/icons/BugReportOutlined";

import _ from "lodash";
import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import Divider from "@material-ui/core/Divider";
import ListItemText from "@material-ui/core/ListItemText";
import ListItemAvatar from "@material-ui/core/ListItemAvatar";
import Avatar from "@material-ui/core/Avatar";
import Typography from "@material-ui/core/Typography";

const useStyles = makeStyles(theme => ({
  root: {
    width: "100%",
    maxWidth: 360,
    backgroundColor: theme.palette.background.paper
  },
  inline: {
    display: "inline"
  }
}));

const appearanceLabelStr = ({
  name,
  scientificName,
  systematicLevel
} = `${name} (${scientificName})`);

const Appearance = ({ appearance, labels }) => {
  const appearanceLabels = appearance.appearanceLabels;
  return (
    <ListItem alignItems="flex-start">
      <ListItemIcon>
        <BugReportOutlinedIcon />
      </ListItemIcon>
      <ListItemText
        primary={appearanceLabelStr(labels.byKey[appearanceLabels[0].labelId])}
        secondary={appearanceLabels.map(id =>
          appearanceLabelStr(labels.byKey[id])
        )}
      />
    </ListItem>
  );
};

const intersperse = (elements, makeInter, makeElement) =>
  flatMap(elements, (a, i) =>
    i ? [makeInter(i), makeElement(a)] : [makeElement(a)]
  );

// export default function AlignItemsList() {
//   const classes = useStyles();
// const inter = ();
//   return (
//     <List className={classes.root}>
//     {/* {_.flatMap(arr, (a, i) => i ? [<Divider key={'divider-'+i} variant="inset" component="li" />, a] : [a]))} */}

//     </List>
//   );
// }

// import React from "react";
// import { makeStyles } from "@material-ui/core/styles";
// import { connect } from "react-redux";

// import * as a from "../../actions";

// import Annotation from "react-image-annotation";
// import Rectangle from "../Rectangle";
// import Radio from "@material-ui/core/Radio";
// import RadioGroup from "@material-ui/core/RadioGroup";
// import FormControlLabel from "@material-ui/core/FormControlLabel";
// import FormControl from "@material-ui/core/FormControl";
// import FormLabel from "@material-ui/core/FormLabel";
// import Grid from "@material-ui/core/Grid";

// import IconButton from "@material-ui/core/IconButton";

// import LabelIcon from "@material-ui/icons/Label";
// import DeleteIcon from "@material-ui/icons/Delete";
// import NavigateNextIcon from "@material-ui/icons/NavigateNext";
// import NavigateBeforeIcon from "@material-ui/icons/NavigateBefore";
// import Table from "@material-ui/core/Table";
// import TableBody from "@material-ui/core/TableBody";
// import TableCell from "@material-ui/core/TableCell";
// import TableContainer from "@material-ui/core/TableContainer";
// import TableRow from "@material-ui/core/TableRow";
// import Paper from "@material-ui/core/Paper";

// import Card from "@material-ui/core/Card";
// import CardHeader from "@material-ui/core/CardHeader";
// import CardContent from "@material-ui/core/CardContent";

// const LabelList = ({
//   appearances,
//   activeId,
//   classes,
//   onDelete,
//   onActive,
//   labels
// }) => {
//   return (
//     <TableContainer component={Paper}>
//       <Table
//         className={classes.labelListTable}
//         size="small"
//         aria-label="a dense table"
//       >
//         <TableBody>
//           {appearances.allIds.map(id => (
//             <TableRow
//               key={"label-" + id}
//               selected={activeId == id}
//               onMouseEnter={() => onActive(id)}
//               onMouseLeave={() => onActive(null)}
//             >
//               <TableCell padding="checkbox">
//                 <LabelIcon />
//               </TableCell>
//               <TableCell align="right">
//                 {labels.byKey[appearances.byKey[id].labelId].name}
//               </TableCell>
//               <TableCell padding="checkbox">
//                 <IconButton aria-label="delete" onClick={() => onDelete(id)}>
//                   <DeleteIcon />
//                 </IconButton>
//               </TableCell>
//             </TableRow>
//           ))}
//         </TableBody>
//       </Table>
//     </TableContainer>
//   );
// };
