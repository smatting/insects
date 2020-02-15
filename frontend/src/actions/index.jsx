export const updateView = view => {
  return {
    type: "VIEW_UPDATE",
    view,
    server: true
  };
};

export const updateSearch = search => {
  return {
    type: "SEARCH_UPDATE",
    search,
    server: true
  };
};

export const deleteAppearance = appearanceId => {
  return {
    type: "APPEARANCE_DELETE",
    appearanceId,
    server: true
  };
};

export const addAppearance = ({ frameId, appearance }) => {
  return {
    type: "APPEARANCE_ADD",
    frameId,
    appearance,
    server: true
  };
};

export const selectCollectionFrame = (collectionId, frameIdx) => {
  return {
    type: "COLLECTIONFRAME_SELECT",
    collectionId,
    frameId,
    server: true
  };
};
