import React from "react";
import { makeStyles } from "@material-ui/core/styles";

import Annotation from "react-image-annotation";
import Rectangle from "./Rectangle";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormControl from "@material-ui/core/FormControl";
import FormLabel from "@material-ui/core/FormLabel";
import Grid from "@material-ui/core/Grid";

const useStyles = makeStyles({
  img: { height: "100%" },
  speciesControl: {}
});

const renderHighlight = ({ key, annotation, active }) => (
  <>
    <div
      style={{
        position: "absolute",
        left: `${annotation.geometry.x}%`,
        top: `${annotation.geometry.y}%`
      }}
    >
      {annotation.data.species.name}
    </div>
    <Rectangle key={key} annotation={annotation} active={active} />
  </>
);

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
        {species.map(s => (
          <FormControlLabel
            value={s.id}
            control={<Radio />}
            label={s.name}
            key={"species-radio-" + s.id}
          />
        ))}
      </RadioGroup>
    </FormControl>
  );
};

const dummyData = {
  url:
    "http://storage.googleapis.com/eco1/frames/cam1/2019-11-15/19/01-20191115192717-02.jpg",
  species: [
    { name: "Heimchen", id: "sdasd" },
    { name: "Wander-Heuschrecken", id: "asfaa" },
    { name: "Wüsten-Heuschrecken", id: "hgawd" }
  ]
};

const Frame = ({ url = dummyData.url, species = dummyData.species }) => {
  const classes = useStyles();
  const [annotations, setAnnotations] = React.useState([]);
  const [annotation, setAnnotation] = React.useState({});
  const [activeSpecies, setActiveSpecies] = React.useState(species[0]["id"]);
  const species_by_key = _.keyBy(species, "id");

  const onSubmit = () => {
    const { geometry, data } = annotation;
    console.log(annotation);
    setAnnotation({});
    setAnnotations(
      annotations.concat({
        geometry,
        data: {
          species: species_by_key[activeSpecies],
          id: Math.random()
        }
      })
    );
  };

  const onSpeciesChange = (e, id) => {
    console.log(e, id);
    setActiveSpecies(id);
  };

  return (
    <Grid container justify="space-between" spacing={1} alignItems="flex-start">
      <Grid container item xs={9} spacing={1}>
        <Annotation
          className={classes.img}
          src={url}
          alt="Test"
          renderHighlight={renderHighlight}
          annotations={annotations}
          value={annotation}
          onChange={setAnnotation}
          onMouseUp={onSubmit}
          disableOverlay={true}
          disableEditor={true}
        />
      </Grid>
      <Grid container item xs={3} spacing={1}>
        <SpeciesSelector
          classes={classes}
          species={species}
          activeSpecies={activeSpecies}
          onSpeciesChange={onSpeciesChange}
        />
      </Grid>
    </Grid>
  );
};

export default Frame;
