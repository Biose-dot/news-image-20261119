// news-image-20261119 entrypoint: deliver the poster to the grader.
//
// The entry is one image, entry.png beside this file: a 1024x1024 PNG
// poster summing up the world news of Thursday 19 November 2026 (drawn
// from source by build_image.py, which is a build-time tool only). The
// grader runs this program offline and reads /output/entry.png, so the
// job here is a faithful copy: create the output directory, copy the
// bytes unchanged, then verify the copy's size matches the original
// before exiting successfully.
//
// Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const posterPath = fileURLToPath(new URL('./entry.png', import.meta.url));
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const targetPath = join(outputDir, 'entry.png');

// Refuse to deliver a corrupt poster: the gate reads the file as a PNG or
// a JPEG by its first bytes, so check the signature before copying.
const head = readFileSync(posterPath).subarray(0, 4);
const isPng = head[0] === 0x89 && head[1] === 0x50 && head[2] === 0x4e && head[3] === 0x47;
const isJpeg = head[0] === 0xff && head[1] === 0xd8;
if (!isPng && !isJpeg) {
  throw new Error('entry.png is neither a PNG nor a JPEG by its first bytes');
}

mkdirSync(outputDir, { recursive: true });
copyFileSync(posterPath, targetPath);

const expected = statSync(posterPath).size;
const actual = statSync(targetPath).size;
if (actual !== expected) {
  throw new Error(`incomplete copy: ${actual} of ${expected} bytes written`);
}
console.log(`entry.png delivered to ${targetPath} (${actual} bytes)`);
