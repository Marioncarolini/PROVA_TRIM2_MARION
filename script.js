const meses = [
  'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 
  'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
];

for (let i = 0; i < meses.length; i++) {
  console.log(`${meses[i]}`);
  if (meses[i] === 'novembro') {
    console.log(`nasci em ${meses[i]}`)
    break;
    
  }
}
