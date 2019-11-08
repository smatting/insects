export const updateView = view => {
  return {
    type: "VIEW_UPDATE",
    view,
    server: true
  };
};
