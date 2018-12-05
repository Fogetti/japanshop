import React, { Component } from 'react';
import {
  Label,
  Table,
  Placeholder,
  Header,
  Container,
  Image
} from 'semantic-ui-react';
import AppHeader from './AppHeader';
import { connect } from 'react-redux';
import { loadProducts } from './products/LoadProductsAction';

import logo from './logo.svg';
import './App.css';

const Home = (props) => <div>
  <Container>
    <Table celled>
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell>Category</Table.HeaderCell>
          <Table.HeaderCell>Name</Table.HeaderCell>
          <Table.HeaderCell>Description</Table.HeaderCell>
        </Table.Row>
      </Table.Header>

      <Table.Body>
        {props.stillLoading ? (
          <Table.Row>
            {[...Array(3).keys()].map((value, index) => {
              return (
                <Table.Cell key={index}>
                  <Placeholder>
                    <Placeholder.Paragraph>
                      <Placeholder.Line length='medium' />
                      <Placeholder.Line length='short' />
                    </Placeholder.Paragraph>
                  </Placeholder>
                </Table.Cell>
              )
            })}
          </Table.Row>
        ) : (props.products.map(product => {
          return (
            <Table.Row key={product.id}>
              <Table.Cell>
                <Label ribbon>{product.category}</Label>
              </Table.Cell>
              <Table.Cell>
                <Header as='h4' image>
                  <Image rounded size='mini' src={logo} />
                  <Header.Content>
                    {product.name}
                    <Header.Subheader>{product.description}</Header.Subheader>
                  </Header.Content>
                </Header>
              </Table.Cell>
              <Table.Cell>{product.description}</Table.Cell>
            </Table.Row>
          );
        }))}
      </Table.Body>

      <Table.Footer>
        <Table.Row>
        </Table.Row>
      </Table.Footer>
    </Table>
  </Container>
</div>

export class App extends Component {
  componentDidMount() {
    this.props.load();
  }
  render() {
    return (
      <div >
        <AppHeader/>
        {this.props.products && <Home {...this.props} />}
      </div>
    );
  }
}

const mapStateToProps = (state, ownProps) => {
  const products = state.allProducts.products ? state.allProducts.products : undefined;
  const stillLoading = state.allProducts.stillLoading;
  return {
    stillLoading,
    products
  }
};

const mapDispatchToProps = dispatch => {
  return {
    load: async () => {
      await dispatch(loadProducts());
    },
  }
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(App);
