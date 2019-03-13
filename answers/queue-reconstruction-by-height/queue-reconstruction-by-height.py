var reconstructQueue = function(people) {
    var res = [];
    people.sort((p1,p2) => p1[0] === p2[0] ? p1[1] - p2[1] : p2[0] - p1[0]).forEach(p => res.splice(p[1], 0, p));
    return res;
};