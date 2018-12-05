import {
  PRODUCT_BY_CATEGORY_LOAD_START,
  PRODUCT_BY_CATEGORY_LOAD_SUCCEEDED,
  PRODUCT_BY_CATEGORY_LOAD_FAILED
} from '../constants/LoadProductsByCategoryTypes';

export default (state = { stillLoading: true }, action) => {
  switch(action.type) {
    case PRODUCT_BY_CATEGORY_LOAD_START:
      return { ...state, stillLoading:true };
    case PRODUCT_BY_CATEGORY_LOAD_SUCCEEDED:
      return { ...state, stillLoading:false, products:action.response.products };
    case PRODUCT_BY_CATEGORY_LOAD_FAILED:
      return { ...state, stillLoading:false };
    default:
      return state;
  }
}