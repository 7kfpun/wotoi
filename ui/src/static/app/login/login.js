angular.module('login', []).controller('loginController', function(
  $scope, $rootScope, api, authState, ipCookie, $location
) {

  $scope.title = 'login';

  $scope.authState = authState;

  $scope.getCredentials = function(){
    return {username: $scope.username, password: $scope.password};
  };

  $scope.login = function(){
    api.auth.login($scope.getCredentials()).
      $promise.
      then(function(data){
      authState.user = data.username;
      ipCookie('user', data.username);
      $location.path("/admin");
    })
    .catch(function(data){
      alert(data.data.detail);
    });
  };

  $scope.logout = function(){
    api.auth.logout(function(){
      authState.user = undefined;
    });
  };

  $scope.register = function($event){
    $event.preventDefault();
    api.users.create($scope.getCredentials()).
      $promise.
      then($scope.login).
      catch(function(data){
      alert(data.data.username);
    });
  };

});
