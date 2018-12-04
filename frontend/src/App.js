import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import {
  Icon,
  Label,
  Menu,
  Table,
  List,
  Grid,
  Placeholder,
  Segment,
  Header,
  Container,
  Image
} from 'semantic-ui-react'
import { connect } from 'react-redux';
import { loadProducts } from './products/LoadProductsAction';
import { loadCategories } from './products/LoadCategoriesAction';
import { logout } from './generic/LogoutAction';

import logo from './logo.svg';
import './App.css';

class App extends Component {
  componentDidMount() {
    const { load } = this.props;
    load();
  }
  render() {
    return (
      <div >
        <Header>
          {this.props.categories.stillLoading ? (
            <Menu inverted>
            {[...Array(5).keys()].map((value, index) => {
              return (
                <Menu.Item key={index}>
                  <Placeholder inverted>
                    <Placeholder.Paragraph>
                      <Placeholder.Line length="medium">
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                      </Placeholder.Line>
                    </Placeholder.Paragraph>
                  </Placeholder>
                </Menu.Item>
              )
              })}
              <Menu.Item>Log out</Menu.Item>
            </Menu>) : (
            <Menu inverted>
              {this.props.categories.map(category => {
                return (<Menu.Item key={category.id} name={category.name} active={category.name === 'home'} onClick={this.handleItemClick} />)
              })}
              <a href="#" onClick={this.props.logout}><Menu.Item>Log out</Menu.Item></a>
            </Menu>
          )}
        </Header>
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
              {this.props.products.stillLoading ? (
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
              ) : (this.props.products.map(product => {
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
    );
  }
}

const mapStateToProps = (state, ownProps) => {
  const products = state.products.products ? state.products.products : {};
  products.stillLoading = state.products.stillLoading;
  const categories = state.categories.categories ? state.categories.categories : {};
  categories.stillLoading = state.categories.stillLoading;
  return {
    categories,
    products
  }
};

const mapDispatchToProps = dispatch => {
  return {
    load: async () => {
      await dispatch(loadProducts());
      await dispatch(loadCategories());
    },
    logout: async () => {
      await dispatch(logout());
    }
  }
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(App);
