function solution(q, r, code) {
    var answer = '';
    let codesol = [...code].map((_,idx)=>idx%q==r ? _ : "")
    return codesol.join("");
}