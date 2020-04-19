clearvars; close all; clc;

%% File's directory and the list of file names

path = 'wavedec/';
%path = 'wavedecun/';
svpath = '../../zfiles/';

files = dir(path);
files = rmfield(files, 'folder');
files = rmfield(files, 'bytes');
files = rmfield(files, 'datenum');
files = rmfield(files, 'isdir');
files = rmfield(files, 'date');
files(1:2) = [];
files = {files.name}.';

feas = zeros(length(files),46);
feas2 = zeros(length(files),29);
for i=1:length(files)

    %% Extracting coefficients
    disp(['Extracting statistical features in ' files{i,1}]);
    load([path files{i}]);
    [d1,d2,d3,d4,d5,d6,d7] = detcoef(coef,leng,[1,2,3,4,5,6,7]);
    a7 = appcoef(coef,leng,'db2',7);
    
    %% Get statistical features from coefficients
    
    %Mean of the absolute value from each subband coefficient
    f1d1 = meanabs(d1);
    f1d2 = meanabs(d2);
    f1d3 = meanabs(d3);
    f1d4 = meanabs(d4);
    f1d5 = meanabs(d5);
    f1d6 = meanabs(d6);
    f1d7 = meanabs(d7);
    f1a7 = meanabs(a7);
    
    %Average power of each subband
    f2d1 = sqrt((1/length(d1))*sum(d1.^2));
    f2d2 = sqrt((1/length(d2))*sum(d2.^2));
    f2d3 = sqrt((1/length(d3))*sum(d3.^2));
    f2d4 = sqrt((1/length(d4))*sum(d4.^2));
    f2d5 = sqrt((1/length(d5))*sum(d5.^2));
    f2d6 = sqrt((1/length(d6))*sum(d6.^2));
    f2d7 = sqrt((1/length(d7))*sum(d7.^2));
    f2a7 = sqrt((1/length(a7))*sum(a7.^2));
    
    %Standard deviation of each subband coefficient
    f3d1 = std(d1);
    f3d2 = std(d2);
    f3d3 = std(d3);
    f3d4 = std(d4);
    f3d5 = std(d5);
    f3d6 = std(d6);
    f3d7 = std(d7);
    f3a7 = std(a7);
    
    %Ratio of mean absolute value of the adjacent subband
    f4d32 = f1d3/f1d2;
    f4d43 = f1d4/f1d3;
    f4d54 = f1d5/f1d4;
    f4d65 = f1d6/f1d5;
    f4d76 = f1d7/f1d6;
    f4a7d7 = f1a7/f1d7;
    
    %Skewness of each subband coefficient
    f5d1 = skewness(d1);
    f5d2 = skewness(d2);
    f5d3 = skewness(d3);
    f5d4 = skewness(d4);
    f5d5 = skewness(d5);
    f5d6 = skewness(d6);
    f5d7 = skewness(d7);
    f5a7 = skewness(a7);
    
    %Kurtosis of each subband coefficient
    f6d1 = kurtosis(d1);
    f6d2 = kurtosis(d2);
    f6d3 = kurtosis(d3);
    f6d4 = kurtosis(d4);
    f6d5 = kurtosis(d5);
    f6d6 = kurtosis(d6);
    f6d7 = kurtosis(d7);
    f6a7 = kurtosis(a7);
    
    %%Arrange the features
    fea = [f1a7,f2a7,f3a7,f4a7d7,f5a7,f6a7,...
           f1d7,f2d7,f3d7,f4d76,f5d7,f6d7,...
           f1d6,f2d6,f3d6,f4d65,f5d6,f6d6,...
           f1d5,f2d5,f3d5,f4d54,f5d5,f6d5,...
           f1d4,f2d4,f3d4,f4d43,f5d4,f6d4,...
           f1d3,f2d3,f3d3,f4d32,f5d3,f6d3,...
           f1d2,f2d2,f3d2,f5d2,f6d2,...
           f1d1,f2d1,f3d1,f5d1,f6d1];
    
    fea2 = [f1d7,f2d7,f3d7,f4d76,f5d7,f6d7,...
           f1d6,f2d6,f3d6,f4d65,f5d6,f6d6,...
           f1d5,f2d5,f3d5,f4d54,f5d5,f6d5,...
           f1d4,f2d4,f3d4,f4d43,f5d4,f6d4,...
           f1d3,f2d3,f3d3,f5d3,f6d3];
	
    feas(i,:) = fea;
    save([svpath 'dwt7db2_fea.mat'],'feas','-v7.3');
    %save([svpath 'dwt7db2unpre_fea.mat'],'feas','-v7.3');
    
end



