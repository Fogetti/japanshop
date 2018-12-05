import React from 'react';

import {
  Icon,
  Label,
  Button,
  Item,
  Container,
} from 'semantic-ui-react';

import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import { loadProductsByCategory } from './LoadProductsByCategoryAction';

export class ProductList extends React.Component {
  componentDidMount() {
    this.props.history.listen((location, action) => {
        console.log(action, location.pathname, location.state);
        this.props.loadByCategory(location.pathname.substring(1));
    });
  }
  
  render() {
    return (
      <Container>
        <Item.Group divided>
          {this.props.products && this.props.products.map(product => {
            return (
              <Item key={product.id}>
                <Item.Image src={product.image1} />
                <Item.Content>
                  <Item.Header as='a'>{product.name}</Item.Header>
                  <Item.Meta>
                    <span>{product.id}</span>
                  </Item.Meta>
                  <Item.Description>
                    {product.description}
                  </Item.Description>
                  <Item.Extra>
                    <Button floated='right' primary>
                      Details
                      <Icon name='chevron right' />
                    </Button>
                    <Label>{product.category}</Label>
                  </Item.Extra>
                </Item.Content>
              </Item>
            )
          })}
        </Item.Group>
      </Container>
    );
  }
}

const mapStateToProps = (state, ownProps) => {
  const products = state.productsByCategories.products ? state.productsByCategories.products : [];
  products.stillLoading = state.productsByCategories.stillLoading;
  return {
    products,
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    loadByCategory: async (category) => {
      await dispatch(loadProductsByCategory(category));
    }
  };
}

export default withRouter(connect(
  mapStateToProps,
  mapDispatchToProps
)(ProductList));