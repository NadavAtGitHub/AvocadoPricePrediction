let app = angular.module("myApp", ["ngRoute"]);

// app.config(function($routeProvider) {
//     $routeProvider
//     .when("/", {
//         template: 'hello'
//     })
//     .when("/red", {
//         template: 'red'
//     })
//     .when("/green", {
//         template: 'green'
//     })
//     .when("/blue", {
//         template: 'blue'
//     });
// });

let avocadoForm = angular.module("avocadoForm", []);
avocadoForm.controller("AvocadoFormController", ["$scope", "$http", function ($scope, $http) {
        console.log("entered controller");
        $scope.formFields = [
            {
                "name": "total_volume",
                "type": "number",
                "required": "required",
            },
            {
                "name": "num_plu_4046",
                "type": "number",
                "required": "required",
            },
            {
                "name": "num_plu_4225",
                
                "type": "number",
                "required": "required",
            },{
                "name": "num_plu_4770",
                "type": "number",
                "required": "required",
            },{
                "name": "total_bags",
                "type": "number",
                "required": "required",
            },{
                "name": "small_bags",
                "type": "number",
                "required": "required",
            },{
                "name": "medium_bags",
                "type": "number",
                "required": "required",
            },{
                "name": "large_bags",
                "type": "number",
                "required": "required",
            },{
                "name": "extra_large_bags",
                "type": "number",
                "required": "required",
            },
            {
                "name": "type",
                "type": "text",
                "required": "required",
            },{
                "name": "year",
                "type": "number",
                "required": "required",
            },{
                "name": "region",
                "type": "text",
                "required": "required",
            },
        ];

        $scope.formData = {};
        $scope.url = "/predict/";
        // TODO: rename to remove word master
        $scope.master = {};
        $scope.avocadoTypes = [
            "conventional",
            "organic",
        ];

        $scope.regions = [
          "Albany",
          "Atlanta",
          "BaltimoreWashington",
        ];

        const MIN_YEAR = 1900;
        const MAX_YEAR = 2020;

        $scope.avocadoYears = [];
        for (let i = MIN_YEAR; i < MAX_YEAR; i++) {
            $scope.avocadoYears.push(i);
        }

        console.log($scope.avocadoYears);

        $scope.update = function (avocadoOrder) {
            console.log("Update called");
            $scope.master = angular.copy(avocadoOrder);
            console.log($scope.master);

            let config = {
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                }
            };
            $http.post($scope.url, $scope.master, config.headers).then(
                function(response) {
                    console.log(response);
                    $scope.price_prediction = response.data.price;
                },
                // Second handles failure
                function(response) {
                    console.log("failure " + response);
                    $scope.response = response;
                }
            );
        };

        $scope.reset = function (form) {
            if (form) {
                form.$setPristine();
                form.$setUntouched();
            }
            $scope.avocadoOrder = angular.copy($scope.master);
        };

        $scope.submit = function(form) {
            console.log("code change seen");
            console.log($scope.formFields);
            for (let field of $scope.formFields) {
                console.log("field " + field);
                $scope.formData[field.name] =  form[field.name];
            }
            console.log("master2" + $scope.formData);

        };
        $scope.reset();
    }]);

