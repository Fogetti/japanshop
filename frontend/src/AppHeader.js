import React from 'react';

import {
  Menu,
  Placeholder,
  Header,
  Container,
} from 'semantic-ui-react';

import { connect } from 'react-redux';
import { logout } from './generic/LogoutAction';
import { loadCategories } from './products/LoadCategoriesAction';
import { Route, Link } from 'react-router-dom';
import ProductList from './products/ProductList';

export class AppHeader extends React.Component {
  componentDidMount() {
    this.props.load();
  }

  render() {
    return (
      <Header>
        {this.props.categories.stillLoading ? (
          <Container>
            <Menu stackable>
            {[...Array(5).keys()].map((value, index) => {
              return (
                <Menu.Item key={index}>
                  <Placeholder>
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
            </Menu>
          </Container>) : (
          <Container>
            <Menu stackable>
              {this.props.categories.map(category => {
                return (
                  <Menu.Item
                    key={category.id}
                    active={category.name === 'home'}
                    onClick={this.handleItemClick}>
                    <Link to={`/${category.name}`}>{category.name}</Link>
                  </Menu.Item>);
              })}
              <a href="#" onClick={this.props.logout}><Menu.Item>Log out</Menu.Item></a>
            </Menu>
            <Route path="/" exact component={ProductList} key="default" />
            {this.props.categories.map(category => {
              return (
                <Route path={`/${category.name}`} component={ProductList} key={category.id} />
              );
            })}
          </Container>
        )}
      </Header>
    );
  }
}

const mapStateToProps = (state, ownProps) => {
  const categories = state.categories.categories ? state.categories.categories : {};
  categories.stillLoading = state.categories.stillLoading;
  return {
    categories,
  }
};

const mapDispatchToProps = dispatch => {
  return {
    load: async () => {
      await dispatch(loadCategories());
    },
    logout: async () => {
      await dispatch(logout());
    },
  }
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(AppHeader);
