import { PRODUCT_LOAD_START, PRODUCT_LOAD_SUCCEEDED, PRODUCT_LOAD_FAILED } from '../constants/LoadProductTypes';

export function loadProducts() {
  return {
    // Types of actions to emit before and after
    types: [PRODUCT_LOAD_START, PRODUCT_LOAD_SUCCEEDED, PRODUCT_LOAD_FAILED],
    // Check the cache (optional):
    shouldCallAPI: state => true,
    // Perform the fetching:
    callAPI: () => fetch('/api/products/')
      .then(function(response) {
        return response.json();
      })
      .then(function(products) {
        return {
          type: PRODUCT_LOAD_SUCCEEDED,
          products
        };
      }),
    // Arguments to inject in begin/end actions
    payload: {  }
  }
}