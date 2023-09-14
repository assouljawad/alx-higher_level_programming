#!/usr/bin/node
exports.esrever = function (list) {
  const List = [];
  for (let i = list.length - 1; i > -1; i--) {
    List[list.length - i - 1] = list[i];
  }
  return List;
};
