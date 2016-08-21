function initSearchController(options){

    angular.module('search', []).controller('searchController', function ($http) {
        var sc = this;
        sc.recipies = [];
        sc.name = "";
        sc.fetchingRecipies = false;
        sc.searchMade = false;

        function searchRecipies(name){
            var url = options.searchUrl + "?name=" + name + "&format=json";
            sc.fetchingRecipies = true;
            sc.searchMade = true;
            $http.get(url).success(function (response) {
                sc.recipies = response;
                sc.fetchingRecipies = false;
            });
        }

        sc.onSearchClick = function(){
            searchRecipies(sc.name)
        }
    })
}