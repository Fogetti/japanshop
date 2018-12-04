import {
  CATEGORY_LOAD_START,
  CATEGORY_LOAD_SUCCEEDED,
  CATEGORY_LOAD_FAILED
} from '../constants/LoadCategoryTypes';

export default (state = { stillLoading: true }, action) => {
  switch(action.type) {
    case CATEGORY_LOAD_START:
      return { ...state, stillLoading:true };
    case CATEGORY_LOAD_SUCCEEDED:
      return { ...state, stillLoading:false, categories:action.response.categories };
    case CATEGORY_LOAD_FAILED:
      return { ...state, stillLoading:false };
    default:
      return state;
  }
}