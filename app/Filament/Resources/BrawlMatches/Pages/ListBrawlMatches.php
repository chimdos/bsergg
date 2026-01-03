<?php

namespace App\Filament\Resources\BrawlMatches\Pages;

use App\Filament\Resources\BrawlMatches\BrawlMatchResource;
use Filament\Actions\CreateAction;
use Filament\Resources\Pages\ListRecords;

class ListBrawlMatches extends ListRecords
{
    protected static string $resource = BrawlMatchResource::class;

    protected function getHeaderActions(): array
    {
        return [
            CreateAction::make(),
        ];
    }
}
