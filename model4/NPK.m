function [y1] = NPK(x1)
%NPK neural network simulation function.
%
% Generated by Neural Network Toolbox function genFunction, 20-Aug-2018 21:48:32.
% 
% [y1] = NPK(x1) takes these arguments:
%   x = 3xQ matrix, input #1
% and returns:
%   y = 1xQ matrix, output #1
% where Q is the number of samples.

%#ok<*RPMT0>

% ===== NEURAL NETWORK CONSTANTS =====

% Input 1
x1_step1.xoffset = [30;0;0];
x1_step1.gain = [0.00803212851405622;0.0222222222222222;0.00625];
x1_step1.ymin = -1;

% Layer 1
b1 = [-0.41620399547470982027;0.83039380987983124616;0.04795080929028772837];
IW1_1 = [-0.46811828005830480315 0.23129136013410009354 0.31193490738936180406;-0.6522390326753255696 0.80208594857773063413 -0.20265800398193886678;-1.3567954868582741135 2.0084197963341714477 0.8917447401720929312];

% Layer 2
b2 = 0.69872185379061901855;
LW2_1 = [-0.80257414692992756766 -1.3660225925001161507 1.0838846004783568855];

% Output 1
y1_step1.ymin = -1;
y1_step1.gain = 0.0761324704986677;
y1_step1.xoffset = 12.09;

% ===== SIMULATION ========

% Dimensions
Q = size(x1,2); % samples

% Input 1
xp1 = mapminmax_apply(x1,x1_step1);

% Layer 1
a1 = tansig_apply(repmat(b1,1,Q) + IW1_1*xp1);

% Layer 2
a2 = repmat(b2,1,Q) + LW2_1*a1;

% Output 1
y1 = mapminmax_reverse(a2,y1_step1);
end

% ===== MODULE FUNCTIONS ========

% Map Minimum and Maximum Input Processing Function
function y = mapminmax_apply(x,settings)
  y = bsxfun(@minus,x,settings.xoffset);
  y = bsxfun(@times,y,settings.gain);
  y = bsxfun(@plus,y,settings.ymin);
end

% Sigmoid Symmetric Transfer Function
function a = tansig_apply(n,~)
  a = 2 ./ (1 + exp(-2*n)) - 1;
end

% Map Minimum and Maximum Output Reverse-Processing Function
function x = mapminmax_reverse(y,settings)
  x = bsxfun(@minus,y,settings.ymin);
  x = bsxfun(@rdivide,x,settings.gain);
  x = bsxfun(@plus,x,settings.xoffset);
end
