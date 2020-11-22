var mincostTickets = function(days, costs) {
    let lentravel = days[-1];
    let ticket = new Array(lentravel);
    ticket.fill(0);
    for (let i=0; i<days.length;i++) {
        ticket[days[i]-1] = 1;
    }

    function price (n) {
        if (n==-1) return 0
        if (ticket[n] ==0) return price(n-1)
        let a1 = Math.max(-1,n-1);
        let a2 = Math.max(-1,n-7);
        let a3 = Math.max(-1, n-15);
        let kq;
        kq = Math.min(price(a1) + costs[0], price(a2) + costs[1], price(a3) + costs[2]);
        return kq;
    }
    return price(lentravel-1);
};

let days = [1,2,3,4,5,6,7,8,9,10,30,31]; let costs = [2,7,15]

console.log(mincostTickets(days,costs))

