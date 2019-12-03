data = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,2,23,10,27,1,27,5,31,1,31,6,35,1,6,35,39,2,39,13,43,1,9,43,47,2,9,47,51,1,51,6,55,2,55,10,59,1,59,5,63,2,10,63,67,2,9,67,71,1,71,5,75,2,10,75,79,1,79,6,83,2,10,83,87,1,5,87,91,2,9,91,95,1,95,5,99,1,99,2,103,1,103,13,0,99,2,14,0,0];

for(i = 0; i <= data.length;){
    if(data[i] == 1){
        var output = data[i + 3];
        var input1 = data[i + 1];
        var input2 = data[i + 2];
        data[output] = data[input1] + data[input2];
    }
    else if(data[i] == 2){
        var output = data[i + 3];
        var input1 = data[i + 1];
        var input2 = data[i + 2];
        data[output] = data[input1] * data[input2];
    }
    else if(data[i] == 99){
        console.log(data);
    }
    i += 4;
}


// for($i = 0; $i <= $totalElements;) {
//     if($data[$i] == 1) {
//       $outputElement = $data[$i + 3];
//       $input1 = $data[$i + 1];
//       $input2 = $data[$i + 2];
//       $data[$outputElement] = addOperand($data[$input1], $data[$input2]);
//     } elseif($data[$i] == 2) {
//       $outputElement = $data[$i + 3];
//       $input1 = $data[$i + 1];
//       $input2 = $data[$i + 2];
//       $data[$outputElement] = multiplyOperand($data[$input1], $data[$input2]);
//     } elseif($data[$i] == 99) {
//       print_r($data);
//       exit();
//     }
//     $i = $i + 4;
//   }