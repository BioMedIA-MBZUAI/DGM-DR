from torchvision import transforms as T
import torch

def graham(img):
    if torch.rand(1).item() < 0.5:
        return img
    G = T.GaussianBlur(21, sigma=(10,10))(img)
    res = 4 * img.mean(0, keepdim=True) - 4 * G.mean(0, keepdim=True) * img.mean(0, keepdim=True) + 0.5
    return torch.cat([res,res,res])

basic = T.Compose(
    [
        # T.Resize((224, 224)),
        T.ToTensor(),
        # T.Lambda(graham),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)

aug = T.Compose([
        #T.RandomEqualize(0.5),
        T.RandomHorizontalFlip(),
        T.RandomVerticalFlip(),
        T.ColorJitter(0.3, 0.3, 0.3, 0.1),
        T.RandomGrayscale(p=0.2),
        T.RandomAffine(degrees=(-180,180),
                translate=(0.2,0.2)),
        T.GaussianBlur(kernel_size=7, sigma=0.5),
        T.ToTensor(),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ]
)
