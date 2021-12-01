var arr = [200, 100, 300];
arr.splice(2, 0, 10000);
console.log(arr);

/*
  splice(start,deleteCount,item1,item2)
  splice 메서드는 배열의 기존요소를 삭제 또는 교체하거나새 새요소를 추가하여 배열의 내용 변경
  start : 배열의 변경을 시작할 인덱스
  deleteCount : 배열에서 제거할 요소의 수 0일경우 제거되지 않음
  item1,item2... : 배열에 추가할 요소
*/
