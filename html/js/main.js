var app = angular.module('ganetiFront', ['ngMaterial', 'ngAnimate']).controller('mainCtrl', function($scope, $log, $http) {
	var mainNode = "192.168.0.71";
	var baseUrl = "https://" + mainNode + ":5080/2/";
	var baseUrl = "http://192.168.0.40:8888/data/";
	var tabs = [
		{ title: "Main", src:"main.html"},
		{ title: 'Nodes', src:"nodes.html"},
		{ title: 'Instances', src:"instances.html"},
		{ title: 'Networks', src:"networks.html"},
    ];
	$scope.tabs = tabs;

	var hosts = function () {return $http.get("https://" + mainNode +":5080/2/nodes")};

	$scope.reloadData = function () {
    	$http.get(baseUrl + 'instances' ).then(function(r) { $scope.instances = r.data; });
    	$http.get(baseUrl + 'networks' ).then(function(r) { $scope.networks = r.data; });
    	$http.get(baseUrl + 'nodes' ).then(function(r) { $scope.nodes = r.data; });
		console.log($scope.instances);
		console.log($scope.nodes);
	};

	$scope.reloadData();
	setInterval(function () { $scope.reloadData(); } , 10000 );

});



