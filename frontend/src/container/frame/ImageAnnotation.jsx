import React from "react";
import { makeStyles } from "@material-ui/core/styles";

import Annotation from "react-image-annotation";
import Rectangle from "../Rectangle";

const useStyles = makeStyles({
  img: { height: "100%" }
});

const annotationToAppearance = ({ geometry }) => {
  return {
    bboxXmin: geometry.x / 100,
    bboxXmax: (geometry.x + geometry.width) / 100,
    bboxYmin: geometry.y / 100,
    bboxYmax: (geometry.y + geometry.height) / 100
  };
};

const appearanceToAnnotation = (
  { id, bboxXmin, bboxXmax, bboxYmin, bboxYmax, labelId, creatorId },
  labels,
  activeAnnotation
) => {
  return {
    geometry: {
      x: bboxXmin * 100,
      y: bboxYmin * 100,
      width: (bboxXmax - bboxXmin) * 100,
      height: (bboxYmax - bboxYmin) * 100,
      type: "RECTANGLE"
    },
    data: {
      //   labels: labels.byKey[labelId],
      id,
      creator: "Test",
      active: activeAnnotation == id
    }
  };
};

const renderHighlight = ({ key, annotation }) => {
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
        {/* {annotation.data.labels.name} */}
      </div>
      <Rectangle
        key={"rectangle-" + key}
        annotation={annotation}
        active={annotation.data.active}
      />
    </React.Fragment>
  );
};

const ImageAnnotation = ({
  activeAnnotation,
  onAddAppearance,
  appearances,
  frame,
  labels
}) => {
  const [annotation, setAnnotation] = React.useState({});

  const classes = useStyles();

  const annotations = appearances.allIds.map(id =>
    appearanceToAnnotation(appearances.byKey[id], labels, activeAnnotation)
  );

  const onChange = a => {
    if (a != annotation) {
      setAnnotation(a);
      console.log(a);
    }
  };

  const onSubmit = () => {
    if (annotation.geometry) {
      setAnnotation({});
      onAddAppearance(annotationToAppearance(annotation));
    }
  };
  return (
    <Annotation
      className={classes.img}
      src={frame.url}
      renderHighlight={renderHighlight}
      annotations={annotations}
      value={annotation}
      onChange={onChange}
      onMouseUp={onSubmit}
      disableOverlay={true}
      disableEditor={true}
    />
  );
};

export default ImageAnnotation;
