import { LOGOUT_START, LOGOUT_SUCCEEDED, LOGOUT_FAILED } from '../constants/LogoutTypes';

export function logout() {
  return {
    // Types of actions to emit before and after
    types: [LOGOUT_START, LOGOUT_SUCCEEDED, LOGOUT_FAILED],
    // Check the cache (optional):
    shouldCallAPI: state => true,
    // Perform the fetching:
    callAPI: () => fetch('/api/logout/')
      .then(function (response) {
        return response.json();
      })
      .then(function (products) {
        return {
          type: LOGOUT_SUCCEEDED,
          products
        };
      }),
    // Arguments to inject in begin/end actions
    payload: {}
  }
}