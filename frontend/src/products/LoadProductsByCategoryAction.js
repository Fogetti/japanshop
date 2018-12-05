import { PRODUCT_BY_CATEGORY_LOAD_START, PRODUCT_BY_CATEGORY_LOAD_SUCCEEDED, PRODUCT_BY_CATEGORY_LOAD_FAILED } from '../constants/LoadProductsByCategoryTypes';

export function loadProductsByCategory(category) {
  return {
    // Types of actions to emit before and after
    types: [PRODUCT_BY_CATEGORY_LOAD_START, PRODUCT_BY_CATEGORY_LOAD_SUCCEEDED, PRODUCT_BY_CATEGORY_LOAD_FAILED],
    // Check the cache (optional):
    shouldCallAPI: state => true,
    // Perform the fetching:
    callAPI: () => fetch(`/api/products/?category=${category}`)
      .then(function(response) {
        return response.json();
      })
      .then(function(products) {
        return {
          type: PRODUCT_BY_CATEGORY_LOAD_SUCCEEDED,
          products
        };
      }),
    // Arguments to inject in begin/end actions
    payload: {  }
  }
}