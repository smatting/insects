import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import { connect } from "react-redux";

import * as a from "../actions";

import Annotation from "react-image-annotation";
import Rectangle from "./Rectangle";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormControl from "@material-ui/core/FormControl";
import FormLabel from "@material-ui/core/FormLabel";
import Grid from "@material-ui/core/Grid";

import IconButton from "@material-ui/core/IconButton";

import LabelIcon from "@material-ui/icons/Label";
import DeleteIcon from "@material-ui/icons/Delete";
import NavigateNextIcon from "@material-ui/icons/NavigateNext";
import NavigateBeforeIcon from "@material-ui/icons/NavigateBefore";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableContainer from "@material-ui/core/TableContainer";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";

import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import CardContent from "@material-ui/core/CardContent";

const useStyles = makeStyles({
  img: { height: "100%" },
  speciesControl: {},
  labelListTable: {}
});

const renderHighlight = ({ key, annotation, active }) => {
  console.log("hello");
  return (
    <React.Fragment key={"rectangle-fragment-" + key}>
      <div
        key={"rectangle-label-" + key}
        style={{
          position: "absolute",
          left: `${annotation.geometry.x}%`,
          top: `${annotation.geometry.y}%`
        }}
      >
        {annotation.data.species.name}
      </div>
      <Rectangle
        key={"rectangle-" + key}
        annotation={annotation}
        active={annotation.active}
      />
    </React.Fragment>
  );
};

const SpeciesSelector = ({
  classes,
  species,
  activeSpecies,
  onSpeciesChange
}) => {
  return (
    <FormControl component="fieldset" className={classes.speciesControl}>
      <FormLabel component="legend">Species</FormLabel>
      <RadioGroup
        aria-label="species"
        name="species"
        value={activeSpecies}
        onChange={onSpeciesChange}
      >
        {species.allIds.map(s => (
          <FormControlLabel
            value={species.byKey[s].id}
            control={<Radio />}
            label={species.byKey[s].name}
            key={"species-radio-" + species.byKey[s].id}
          />
        ))}
      </RadioGroup>
    </FormControl>
  );
};

const LabelList = ({ annotations, classes, onDelete, onActive }) => {
  return (
    <TableContainer component={Paper}>
      <Table
        className={classes.labelListTable}
        size="small"
        aria-label="a dense table"
      >
        <TableBody>
          {annotations.map((annotation, idx) => (
            <TableRow
              key={"label-" + idx}
              selected={annotation.active}
              onMouseEnter={() => onActive(idx)}
              onMouseLeave={() => onActive(null)}
            >
              <TableCell padding="checkbox">
                <LabelIcon />
              </TableCell>
              <TableCell align="right">
                {annotation.data.species.name}
              </TableCell>
              <TableCell padding="checkbox">
                <IconButton aria-label="delete" onClick={() => onDelete(idx)}>
                  <DeleteIcon />
                </IconButton>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

const dummyData = {
  url:
    "http://storage.googleapis.com/eco1/frames/cam1/2019-11-15/19/01-20191115192717-02.jpg",
  timestamp: "123123",
  species: [
    { name: "Heimchen", id: "sdasd" },
    { name: "Wander-Heuschrecken", id: "asfaa" },
    { name: "Wüsten-Heuschrecken", id: "hgawd" }
  ]
};

const Frame = ({
  species,
  frame,
  appearances,
  onChangeFrame,
  onAddAppearance,
  prevId,
  nextId
}) => {
  console.log(species);
  if (!frame) {
    return null;
  }

  const classes = useStyles();
  const { url, timestamp } = frame;
  const [annotations, setAnnotations] = React.useState([]);
  const [annotation, setAnnotation] = React.useState({});
  const [activeSpecies, setActiveSpecies] = React.useState(species.allIds[0]);
  //   const [activeAnnotation, setActiveAnnotation] = React.useState();
  const species_by_key = _.keyBy(species, "id");

  const onDelete = idx => {
    annotations.splice(idx, 1);
    setAnnotations([...annotations]);
  };

  const onActive = activeIdx => {
    setAnnotations(
      annotations.map((a, idx) => ({ ...a, active: idx == activeIdx }))
    );
  };

  const onChange = a => {
    if (a != annotation) {
      setAnnotation(a);
    }
  };

  const onSubmit = (test, test2) => {
    const { geometry } = annotation;
    console.log("annotation", annotation, test, test2);
    if (geometry) {
      setAnnotation({});
      setAnnotations(
        annotations.concat(
          {
            geometry,
            data: {
              species: species_by_key[activeSpecies],
              id: Math.random()
            }
          }
          //   () => setActiveAnnotation(annotations.length)
        )
      );
    }
  };

  const onSpeciesChange = (e, id) => {
    console.log(e, id);
    setActiveSpecies(id);
  };

  return (
    <Grid container justify="space-between" spacing={1} alignItems="flex-start">
      <Grid container item xs={9} spacing={1}>
        <Card className={classes.card}>
          <CardHeader
            title={timestamp}
            action={
              <>
                <IconButton
                  aria-label="before"
                  onClick={() => onChangeFrame(prevId)}
                >
                  <NavigateBeforeIcon />
                </IconButton>
                <IconButton
                  aria-label="next"
                  onClick={() => onChangeFrame(nextId)}
                >
                  <NavigateNextIcon />
                </IconButton>
              </>
            }
            // subheader="September 14, 2016"
          />
          <CardContent>
            <Annotation
              className={classes.img}
              src={url}
              renderHighlight={renderHighlight}
              annotations={annotations}
              value={annotation}
              onChange={onChange}
              onMouseUp={onSubmit}
              disableOverlay={true}
              disableEditor={true}
            />
          </CardContent>
        </Card>
      </Grid>
      <Grid container item xs={3} spacing={1}>
        <Grid container item xs={12} spacing={1}>
          <SpeciesSelector
            classes={classes}
            species={species}
            activeSpecies={activeSpecies}
            onSpeciesChange={onSpeciesChange}
          />
        </Grid>
        <Grid container item xs={12} spacing={1}>
          {/* <LabelList
            classes={classes}
            annotations={annotations}
            onDelete={onDelete}
            onActive={onActive}
          /> */}
        </Grid>
      </Grid>
    </Grid>
  );
};

// (url = dummyData.url),
//   (species = dummyData.species),
//   (timestamp = dummyData.timestamp);

const createFrameProps = state => {
  let prevId, nextId, frame;
  const frames = state.collection.frames;
  console.log(state.collection.frames);
  if (frames.allIds.length) {
    frame = frames.byKey[state.collection.currentFrameId];
    const frameIdx = frame.idx;
    if (frameIdx > 0) {
      prevId = frames.allIds[frameIdx - 1];
    }
    if (frameIdx < frames.allIds.length - 1) {
      nextId = frames.allIds[frameIdx + 1];
    }
  }
  return { prevId, nextId, frame, collectionId: state.collection.id };
};

export default connect(
  (state, ownProps) => ({
    ...createFrameProps(state),
    species: state.species,
    appearances: state.appearances
  }),
  (dispatch, ownProps) => ({
    onChangeFrame: id => dispatch(a.selectCollectionFrame(id)),
    onAddAppearance: appearance =>
      dispatch(a.addAppearance({ frameId: frame.id, appearance })),
    onDeleteAppearance: id => dispatch(a.deleteAppearance(id))
  })
)(Frame);
