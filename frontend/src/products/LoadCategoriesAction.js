import { CATEGORY_LOAD_START, CATEGORY_LOAD_SUCCEEDED, CATEGORY_LOAD_FAILED } from '../constants/LoadCategoryTypes';

export function loadCategories() {
  return {
    // Types of actions to emit before and after
    types: [CATEGORY_LOAD_START, CATEGORY_LOAD_SUCCEEDED, CATEGORY_LOAD_FAILED],
    // Check the cache (optional):
    shouldCallAPI: state => true,
    // Perform the fetching:
    callAPI: () => fetch('/api/categories/')
      .then(function(response) {
        return response.json();
      })
      .then(function(categories) {
        return {
          type: CATEGORY_LOAD_SUCCEEDED,
          categories
        };
      }),
    // Arguments to inject in begin/end actions
    payload: {  }
  }
}