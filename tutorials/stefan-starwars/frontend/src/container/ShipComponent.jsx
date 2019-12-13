// @flow
import React from 'react';
import {graphql, createFragmentContainer} from 'react-relay';


import type {ShipComponent_ship} from './__generated__/ShipComponent_ship.graphql.js';


class ShipComponent extends React.Component<ShipComponent_ship> {
    render() {
        return (
              <li>
                <div>
                  <input
                    checked="checked"
                    type="checkbox"
                  />
                  <label>
                    {this.props.name}
                  </label>
                </div>
              </li>
            );
    }
}


export default createFragmentContainer(
  ShipComponent,
  {
    ship: graphql`
      # As a convention, we name the fragment as '<ComponentFileName>_<propName>'
      fragment ShipComponent_ship on Ship {
        id
        name
      }
    `
  },
)
