img=imread('PedegralejoMalaga.jpeg');
size(img); 
ig=rgb2gray(img);
imshow(img)
ig=im2double(ig);

%[*] AVERAGE [*]%



tamano_kernel = 9; %Sizes

kernel = ones(tamano_kernel) / tamano_kernel^2;

img_fltaverage = imfilter(ig, kernel);




figure(10)
subplot(1, 2, 1);
imshow(ig);
title('Photo');
subplot(1, 2, 2);
imshow(img_fltaverage);
title('Photo using Average');




%[*] GAUSSIANO [*]%


img_fgauss1 = imgaussfilt(ig, 0.2);
img_fgauss2 = imgaussfilt(ig, 1);
img_fgauss3 = imgaussfilt(ig, 2);

figure(3)

subplot(2, 2, 1);
imshow(ig);
title('Photo');

subplot(2, 2, 2);
imshow(img_fgauss1);
title('Photo using Gaussian σ=0.2');

subplot(2, 2, 3);
imshow(img_fgauss2);
title('Photo using Gaussian σ=1');

subplot(2, 2, 4);
imshow(img_fgauss3);
title('Photo using Gaussian σ=2');



%[*] Linear disffusion [*]%

Img=imread('PedegralejoMalaga.jpeg');
Img=rgb2gray(Img);
Img=im2double(Img);

[rows, cols,  ~]=size(Img);
mindim=min(rows, cols);

for i=1: mindim
    for j=1:mindim
        sqrImg(i,j)=Img(i,j);
    end
end


N = size(sqrImg,1);    
alpha = 0.3;     
dx = 1;      
numIterations = 100; 

for iteration = 1:numIterations
    du = getRHS(sqrImg, alpha, dx, N);
    sqrImg2 = sqrImg + du;
end


figure(6)
subplot(1, 2, 1);
imshow(sqrImg);
title('Photo');
subplot(1, 2, 2);
imshow(sqrImg2);
title('Photo using Linear diffusion');