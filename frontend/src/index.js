import App from './App';
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware, combineReducers } from 'redux';

import thunk from 'redux-thunk';
import api from './middleware/API';
import allProducts from './products/LoadProductsReducer';
import categories from './products/LoadCategoriesReducer';
import productsByCategories from './products/LoadProductsByCategoryReducer';
import * as serviceWorker from './serviceWorker';
import { BrowserRouter as Router } from 'react-router-dom';

import './index.css';
import 'semantic-ui-css/semantic.min.css';

const reducer = combineReducers({
  allProducts,
  categories,
  productsByCategories
});
const store = createStore(reducer, applyMiddleware(thunk, api));
const rootEl = document.getElementById('root');

ReactDOM.render(
  <Provider store={store}>
    <Router>
      <App />
    </Router>
  </Provider>
, rootEl);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
