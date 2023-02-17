function solution(id_pw, db) {
  const dbArray = db.flat();
  if (dbArray.indexOf(id_pw[0]) === -1) {
    return "fail"
  }

  return dbArray[dbArray.indexOf(id_pw[0]) + 1] === id_pw[1]? "login" : "wrong pw"
}