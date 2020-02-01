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
