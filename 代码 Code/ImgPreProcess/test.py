from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import random


def plot_image(img, ax=None, reverse_rgb=False):
    if ax is None:
        # create new axes
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
    img = img.copy()
    if reverse_rgb:
        img[:, :, (0, 1, 2)] = img[:, :, (2, 1, 0)]
    ax.imshow(img.astype(np.uint8))
    return ax


def plot_bbox(img, bboxes, scores=None, labels=None, thresh=0.5,
              class_names=None, colors=None, ax=None,
              reverse_rgb=False, absolute_coordinates=True):
    if labels is not None and not len(bboxes) == len(labels):
        raise ValueError('The length of labels and bboxes mismatch, {} vs {}'
                         .format(len(labels), len(bboxes)))
    if scores is not None and not len(bboxes) == len(scores):
        raise ValueError('The length of scores and bboxes mismatch, {} vs {}'
                         .format(len(scores), len(bboxes)))

    ax = plot_image(img, ax=ax, reverse_rgb=reverse_rgb)

    if len(bboxes) < 1:
        return ax

    # if isinstance(bboxes, mx.nd.NDArray):
    #     bboxes = bboxes.asnumpy()
    # if isinstance(labels, mx.nd.NDArray):
    #     labels = labels.asnumpy()
    # if isinstance(scores, mx.nd.NDArray):
    #     scores = scores.asnumpy()

    if not absolute_coordinates:
        # convert to absolute coordinates using image shape
        height = img.shape[0]
        width = img.shape[1]
        bboxes[:, (0, 2)] *= width
        bboxes[:, (1, 3)] *= height

    # use random colors if None is provided
    if colors is None:
        colors = dict()
    for i, bbox in enumerate(bboxes):
        if scores is not None and scores.flat[i] < thresh:
            continue
        if labels is not None and labels.flat[i] < 0:
            continue
        cls_id = int(labels.flat[i]) if labels is not None else -1
        if cls_id not in colors:
            if class_names is not None:
                colors[cls_id] = plt.get_cmap('hsv')(cls_id / len(class_names))
            else:
                colors[cls_id] = (random.random(), random.random(), random.random())
        xmin, ymin, xmax, ymax = [int(x) for x in bbox]
        rect = plt.Rectangle((xmin, ymin), xmax - xmin,
                             ymax - ymin, fill=False,
                             edgecolor=colors[cls_id],
                             linewidth=3.5)
        ax.add_patch(rect)
        if class_names is not None and cls_id < len(class_names):
            class_name = class_names[cls_id]
        else:
            class_name = str(cls_id) if cls_id >= 0 else ''
        score = '{:.3f}'.format(scores.flat[i]) if scores is not None else ''
        if class_name or score:
            ax.text(xmin, ymin - 2,
                    '{:s} {:s}'.format(class_name, score),
                    bbox=dict(facecolor=colors[cls_id], alpha=0.5),
                    fontsize=12, color='white')
    return ax


img = Image.open('000054.jpg')
img_array = np.array(img)
ax = plot_image(img_array)

xmin, ymin, xmax, ymax = [int(x) for x in (1, 38, 250, 220)]
colors = dict()
cls_id = 0
colors[cls_id] = plt.get_cmap('hsv')(cls_id)
rect = plt.Rectangle((xmin, ymin), xmax - xmin,
                     ymax - ymin, fill=False,
                     edgecolor=colors[cls_id],
                     linewidth=3.5)
ax.add_patch(rect)
ax.text(xmin, ymin - 2,
        '{:s} {:s}'.format('smoke', '0.972'),
        bbox=dict(facecolor=colors[cls_id], alpha=0.5),
        fontsize=12, color='white')

xmin, ymin, xmax, ymax = [int(x) for x in (110, 50, 230, 200)]
rect = plt.Rectangle((xmin, ymin), xmax - xmin,
                     ymax - ymin, fill=False,
                     edgecolor=colors[cls_id],
                     linewidth=3.5)
ax.add_patch(rect)
ax.text(xmin, ymin - 2,
        '{:s} {:s}'.format('smoke', '0.914'),
        bbox=dict(facecolor=colors[cls_id], alpha=0.5),
        fontsize=12, color='white')

plt.show()
