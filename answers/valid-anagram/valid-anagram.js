var isAnagram = function(s, t) {
    s = s.split('').sort().join(''); 
    t = t.split('').sort().join('');
    return s===t

    
};
// 围观一下大佬的代码
function isAnagram(s, t) {
  const map = {};
  s.split('').map(c => map[c] = map[c] ? map[c] + 1 : 1);
  t.split('').map(c => map[c] = map[c] ? map[c] - 1 : -1);
  return Object.keys(map).every(k => map[k] === 0);
}