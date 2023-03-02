const input = (() => {
  const line = fs.readFileSync('/dev/stdin', 'utf8').toString().split('\n').reverse();
  return () => {
    return line.pop();
  };
})();
